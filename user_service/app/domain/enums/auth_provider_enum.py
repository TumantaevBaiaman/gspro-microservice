import enum


class AuthProvider(enum.Enum):
    email = "email"
    phone = "phone"
    google = "google"
