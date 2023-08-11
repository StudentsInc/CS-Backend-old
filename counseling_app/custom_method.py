from counseling_app.serializer import AppointmentSerializer


def appointment_history(payload):
    serializer = AppointmentSerializer(data=payload)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors
