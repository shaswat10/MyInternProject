from django.shortcuts import render
import requests
from django.views.generic import TemplateView, ListView,DetailView, CreateView, UpdateView, DeleteView, View
from ranuser.models import UserData
from django.urls import reverse_lazy
from django.shortcuts import redirect





class HomeView(TemplateView):
    template_name = "home.html"


# class UserView(CreateView):
def UserView(request):

    response = requests.get('https://randomuser.me/api')
    data = response.json()

    # for i in data['results'][1]['name']:
    #     print(i)
    title = data['results'][0]['name']['title']
    first = data['results'][0]['name']['first']
    last = data['results'][0]['name']['last']


    final_name = " ".join([first,last])

    #############################################
    final_name = ". ".join([title, final_name])          #Final name of the user
    # print(final_name)

    #############################################
    agee = data['results'][0]['dob']['age']               # age of the user
    # print(dob)


    ############################################
    gender = data['results'][0]['gender']                   #Gender
    # print(gender)


    street1 = str(data['results'][0]['location']['street']['number'])
    street2 = str(data['results'][0]['location']['street']['name'])
    city = data['results'][0]['location']['city']
    state = data['results'][0]['location']['state']
    postcode = str(data['results'][0]['location']['postcode'])



    ###############################################
    address = ", ".join([street1,street2, city, state, postcode])  # Final address
    # print(address)


    ###############################################
    email = data['results'][0]['email']                       #Email field
    # print(email)


    ##################################################
    image = data['results'][0]['picture']['medium']            #Image
    # print(image)

    model = UserData

    context_object_name = 'use_data'

    # user_data = {'name': final_name, 'age': agee, 'gender':gender, 'address':address, 'email':email, 'image':image}

    user = UserData.objects.create( name = final_name, age= agee, gender = gender, address=address, email=email, image=image)
    user.save()

    # return render(request,'user_list.html',)

    return redirect('myapp:detail', pk=user.pk)





class UserListView(ListView):
    model = UserData
    context_object_name = 'user_list'
    template_name = 'user_list.html'





class UserDetailView(DetailView):
    model = UserData
    context_object_name = 'user_detail'
    template_name = 'user_detail.html'


class UserDeleteView(DeleteView):
    model = UserData
    context_object_name = 'delete_user'
    template_name = 'user_delete.html'
    success_url = reverse_lazy('myapp:list')
