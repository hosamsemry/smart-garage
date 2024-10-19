from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

# Create your views here.
@api_view(['POST'])
def user_register(request):
    password = request.data.get('password')
    hashed_password = make_password(password)
    request.data['password'] = hashed_password
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    errors_dict = {}
    for field, errors in serializer.errors.items():
        errors_dict[field] = errors[0] if isinstance(errors, list) else errors

    return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    email = request.data.get('mail')
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)

    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'msg': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_users(request):
    all_users = User.objects.all()

    if len(all_users) == 0:
        return Response({'msg':'there are no users'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(all_users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        errors_dict = {}
        for field, errors in serializer.errors.items():
            errors_dict[field] = errors[0] if isinstance(errors, list) else errors

        return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'msg':'user does not exist'},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({'id':id,'msg': 'delete sucess'}, status=status.HTTP_204_NO_CONTENT)
    
    except User.DoesNotExist:
        return Response({'msg':'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def admin_register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    errors_dict = {}
    for field, errors in serializer.errors.items():
        errors_dict[field] = errors[0] if isinstance(errors, list) else errors

    return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def admin_login(request):
    try:
        user = User.objects.get(mail=request.data['mail'], password=request.data['password'])
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({'msg':'Admin does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_admins(request):
    all_users = User.objects.all()

    if len(all_users) == 0:
        return Response({'msg':'there are no admins'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(all_users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_admin(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        errors_dict = {}
        for field, errors in serializer.errors.items():
            errors_dict[field] = errors[0] if isinstance(errors, list) else errors

        return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'msg': 'admin does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_Admin(request, id):
    try:
        admin = User.objects.get(id=id)
        admin.delete()
        return Response({'id':id,'msg': 'delete sucess'}, status=status.HTTP_204_NO_CONTENT)
    
    except User.DoesNotExist:
        return Response({'msg':'admin does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addgarage(request):
    serializer = GarageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    errors_dict = {}
    for field, errors in serializer.errors.items():
        errors_dict[field] = errors[0] if isinstance(errors, list) else errors

    return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_garages(request):
    all_garages = Garage.objects.all()
    json=[]

    if len(all_garages) == 0:
        return Response({'msg':'there are no garages'}, status=status.HTTP_400_BAD_REQUEST)
    
    for garage in all_garages:
        obj=Reservation.objects.filter(garage_id=garage.id,end_time__isnull=True)
        data={'garage_id':garage.id,'title':garage.title,'description':garage.description
            ,'contantnum':garage.contantnum,'price':garage.price,
              'longitude':garage.longitude,'latitude':garage.latitude,
            'totalslots':garage.totalslots,'resreved_slots':len(obj)}
        json.append(data)

    return Response(json, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_garage(request, id):
    try:
        garage = Garage.objects.get(id=id)
        serializer = GarageSerializer(instance=garage, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        errors_dict = {}
        for field, errors in serializer.errors.items():
            errors_dict[field] = errors[0] if isinstance(errors, list) else errors

        return Response(errors_dict, status=status.HTTP_400_BAD_REQUEST)
    
    except Garage.DoesNotExist:
        return Response({'msg':'garage does not exist'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_garage(request, id):
    try:
        garage = Garage.objects.get(id=id)
        garage.delete()
        return Response({'id':id,'msg': 'delete sucess'}, status=status.HTTP_204_NO_CONTENT)

    except Garage.DoesNotExist:
        return Response({'msg':'garage does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def start_reservation(request):
    try:
        reservation = Reservation.objects.get(user_id=request.data['user_id'], end_time__isnull=True)
        return Response({'msg': 'You already have a reservation'}, status=status.HTTP_200_OK)
    
    except Reservation.DoesNotExist:
        try:
            garage = Garage.objects.get(id=request.data['garage_id'])
            objects = Reservation.objects.filter(garage_id=request.data['garage_id'], end_time__isnull=True)

            if len(objects) >= garage.totalslots:
                return Response({'msg': 'You cannot have a reservation in this garage; it is full'}, status=status.HTTP_200_OK)
            
            serializer = StartReservationSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Garage.DoesNotExist:
            return Response({'msg': 'Garage not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def end_reservation(request):
    try:
        reservation = Reservation.objects.get(id=request.data['id'])
        serializer = EndReservationSerializer(instance=reservation, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            reservation.reservation_cost = reservation.calculate_cost()
            reservation.save(update_fields=['reservation_cost'])

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Reservation.DoesNotExist:
        return Response({'msg': 'Reservation not found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getUserCurrentReservation(request,id):
    try:
        reservation=Reservation.objects.get(user_id=id,end_time__isnull=True)
        time=timezone.now()-reservation.start_time
        reservation.reservation_cost=time.total_seconds()/60*reservation.garage_id.price
        reservation.save()
        data = {
            'id': reservation.id,
            'user_id': reservation.user_id.id,
            'start_time': reservation.start_time,
            'reservation_cost': reservation.reservation_cost,
            'garage_id': reservation.garage_id.id,
            'garage_title': reservation.garage_id.title,
            'garage_description': reservation.garage_id.description,
            'price_per_minute': reservation.garage_id.price,
            'longitude': reservation.garage_id.longitude,
            'latitude': reservation.garage_id.latitude
        }
        return Response(data, status=status.HTTP_200_OK)
    
    except Reservation.DoesNotExist:
        return Response({'msg': 'there is no current Reservation for this user'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUserReservations(request,id):
    try:
        reservations = Reservation.objects.filter(user_id=id, end_time__isnull=False)
        reservation_data = []

        for reservation in reservations:
            data={
                'id': reservation.id,
                'user_id': reservation.user_id.id,
                'start_time': reservation.start_time,
                'end_time': reservation.end_time,
                'reservation_cost': reservation.reservation_cost,
                'garage_id': reservation.garage_id.id,
                'garage_title': reservation.garage_id.title,
                'garage_description': reservation.garage_id.description,
                'price_per_minute': reservation.garage_id.price,
                'longitude': reservation.garage_id.longitude,
                'latitude': reservation.garage_id.latitude,
            }
            reservation_data.append(data)

        if len(reservation_data) == 0:
            return Response({'msg': 'no reservations found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(reservation_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_Rservation(request, id):
    try:
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
        return Response({'id':id,'msg': 'delete sucess'}, status=status.HTTP_204_NO_CONTENT)
    
    except Reservation.DoesNotExist:
        return Response({'msg':'reservation does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_reservation(request):
    all_reservations = Reservation.objects.all()

    if len(all_reservations) == 0:
        return Response({'msg':'there are no reservations'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ReservationSerializer(all_reservations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)







