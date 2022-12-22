from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import PetitionsSerializer
from pengajuanEmp.models import Petitions
from datetime import datetime, timedelta

class PengajuanAPIView(APIView):
    serializer_class = PetitionsSerializer

    def get_queryset(self):
        petitions = Petitions.objects.all()
        return petitions
    
    # def get(self, request, *args, **kwargs):
    #     try: 
    #         permission_type = request.query_params["permission_type"]
    #         if permission_type != ' ':
    #             petition  = Petitions.objects.get(permission_type=permission_type)
    #             serializer = PetitionsSerializer(petition)
    #     except:
    #         petitions = self.get_queryset()
    #         serializer = PetitionsSerializer(petitions, many=True)

    #     return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        querySet = Petitions.objects.all()
        
        employee_name = self.request.query_params.get('employee_name', None)
        permission_type = self.request.query_params.get('permission_type', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if employee_name:
            querySet=querySet.filter(employee_name=employee_name)
        if end_date:
            querySet=querySet.filter(end_date=end_date)
        if start_date:
            querySet=querySet.filter(start_date=start_date)
        if permission_type:
            querySet=querySet.filter(permission_type=permission_type)
        # if start_date and end_date :
        #     date_format='%d-%m-%Y'
        #     start_date=datetime.strptime(start_date, date_format)
        #     end_date=datetime.strptime(end_date, date_format)
        #     start_date=end_date+timedelta(days=1)

        #     querySet=querySet.filter(employee_name=employee_name)

        serializer = PetitionsSerializer(querySet, many=True)

        return Response(serializer.data) 
    
    def post(self, request, *args, **kwargs):
        pengajuan_data = request.data
        new_pengajuan = Petitions.objects.create(employee_name=pengajuan_data['employee_name'], division=pengajuan_data['division'], 
                        permission_type=pengajuan_data['permission_type'], reason=pengajuan_data['reason'], 
                        start_date=pengajuan_data['start_date'], end_date=pengajuan_data['end_date'], return_date=pengajuan_data['return_date'])
        new_pengajuan.save()
        serializer = PetitionsSerializer(new_pengajuan)
        return Response(serializer.data)
    

class PengajuanAPIViewID(viewsets.ModelViewSet):
    serializer_class = PetitionsSerializer

    def get_queryset(self):
        petitions = Petitions.objects.all()
        return petitions
    
    def get_ids(self, request, *args, **kwargs):
        ids = request.query_params["id"]
        if ids != None:
                petitions = Petitions.objects(id=ids)
                serializer = PetitionsSerializer(petitions)
        else:
            pett = self.get_queryset()
            serr = PetitionsSerializer(pett, many=True)
        return Response(serializer.data)
    
    def get_name(self, request, *args, **kwargs):
        ids = request.query_params["employee_name"]
        if ids != None:
                petitions = Petitions.objects(employee_name=ids)
                serializer = PetitionsSerializer(petitions)
        else:
            pett = self.get_queryset()
            serr = PetitionsSerializer(pett, many=True)
        return Response(serializer.data)

    
    def post(self, request, *args, **kwargs):
        pengajuan_data = request.data
        new_pengajuan = Petitions.objects.create(employee_name=pengajuan_data['employee_name'], division=pengajuan_data['division'], 
                        permission_type=pengajuan_data['permission_type'], reason=pengajuan_data['reason'], 
                        start_date=pengajuan_data['start_date'], end_date=pengajuan_data['end_date'], return_date=pengajuan_data['return_date'])
        new_pengajuan.save()
        serializer = PetitionsSerializer(new_pengajuan)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            pengajuan = self.get_object()
            pengajuan.delete()
            response_message={"message" : "Petition has been deleted"}
        else:
            response_message={"message" : "Not Allowed"}

        return Response(response_message)