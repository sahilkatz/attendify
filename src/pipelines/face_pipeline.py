import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 


    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []


    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get('face_embedding')
        student_id = student.get('student_id')
        if embedding and student_id is not None:
            X.append(np.array(embedding))
            y.append(int(student_id))

    if len(X) == 0:
        return None

    distinct_labels = set(y)

    # SVC needs at least two classes to fit. With a single enrolled student we
    # skip training entirely and fall back to a pure distance comparison.
    clf = None
    if len(distinct_labels) >= 2:
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        try:
            clf.fit(X, y)
        except ValueError:
            # Never hand back an unfitted classifier - callers would crash on predict()
            clf = None

    return {'clf': clf, 'X': X, "y": y}


def train_classifier():
    get_trained_model.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}


    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    resemblance_threshold = 0.6

    for encoding in encodings:
        if clf is not None:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            # Single known student (or training failed): nearest-neighbour fallback
            distances = [np.linalg.norm(x - encoding) for x in X_train]
            predicted_id = int(y_train[int(np.argmin(distances))])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - encoding)

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
    return detected_student, all_students, len(encodings)