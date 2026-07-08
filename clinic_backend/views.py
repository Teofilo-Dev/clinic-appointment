from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer


# ──────────────────────────────────────────────
#  DOCTOR LOGIN
# ──────────────────────────────────────────────
@api_view(['POST'])
def doctor_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        doctor = Doctor.objects.get(user=user)
    except Doctor.DoesNotExist:
        return Response({'error': 'This account is not registered as a doctor.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = DoctorSerializer(doctor)
    return Response({
        'message': 'Doctor login successful.',
        'role': 'doctor',
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
        'doctor': serializer.data,
    }, status=status.HTTP_200_OK)


# ──────────────────────────────────────────────
#  ADMIN LOGIN
# ──────────────────────────────────────────────
@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.is_staff:
        return Response({'error': 'This account does not have admin privileges.'}, status=status.HTTP_403_FORBIDDEN)

    return Response({
        'message': 'Admin login successful.',
        'role': 'admin',
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
        },
    }, status=status.HTTP_200_OK)


# ──────────────────────────────────────────────
#  RECEPTIONIST LOGIN
# ──────────────────────────────────────────────
@api_view(['POST'])
def receptionist_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    # Receptionists are staff but NOT superusers
    if not user.is_staff or user.is_superuser:
        return Response({'error': 'This account is not registered as a receptionist.'}, status=status.HTTP_403_FORBIDDEN)

    return Response({
        'message': 'Receptionist login successful.',
        'role': 'receptionist',
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
    }, status=status.HTTP_200_OK)


# ──────────────────────────────────────────────
#  PATIENT REQUEST APPOINTMENT (no login needed)
# ──────────────────────────────────────────────
@api_view(['GET'])
def list_doctors(request):
    """Return the list of available doctors so patients can pick one."""
    doctors = Doctor.objects.select_related('user').all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def request_appointment(request):
    """
    Patient submits an appointment request.
    Expected body:
        first_name, last_name, email, phone, date_of_birth (optional),
        doctor_id, appointment_date (ISO datetime), reason (optional)
    """
    from django.contrib.auth.models import User
    from .models import Appointment
    import datetime

    first_name   = request.data.get('first_name', '')
    last_name    = request.data.get('last_name', '')
    email        = request.data.get('email', '')
    phone        = request.data.get('phone', '')
    dob          = request.data.get('date_of_birth')
    doctor_id    = request.data.get('doctor_id')
    appt_date    = request.data.get('appointment_date')
    reason       = request.data.get('reason', '')

    if not all([first_name, last_name, email, doctor_id, appt_date]):
        return Response(
            {'error': 'first_name, last_name, email, doctor_id, and appointment_date are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Create or get a user account for the patient
    username = email.split('@')[0]
    base_username = username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1

    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    if not created:
        user.first_name = first_name
        user.last_name  = last_name
        user.save()

    patient, _ = Patient.objects.get_or_create(user=user, defaults={'phone': phone, 'date_of_birth': dob})

    appointment = Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        appointment_date=appt_date,
        reason=reason,
        status='Pending',
    )

    serializer = AppointmentSerializer(appointment)
    return Response({
        'message': 'Appointment request submitted successfully.',
        'appointment': serializer.data,
    }, status=status.HTTP_201_CREATED)
