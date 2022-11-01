from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LinksmediaForm
from .models import *
from login.models import *
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        check_profrile = Profile.objects.filter(user=request.user).exists()
        if check_profrile:
            obj = Linksmedia.objects.filter(user=request.user)
            profile = Profile.objects.get(user=request.user)
            friends = profile.friends.all()
            for i in friends:
                print(i)
            context = {
                'links': LinksmediaForm,
                'posts': obj,
                'profile': profile,
                'friend_list': friends
            }
            if request.method == "POST":
                title = request.POST.get('title')
                url = request.POST.get('url')
                icon = request.POST.get('icon')
                image = None

                if icon == 'Web Link':
                    image = 'base/assets/img/web.png'
                elif icon == 'Facebook':
                    image = 'base/assets/img/fb.png'
                elif icon == 'Youtube':
                    image = 'base/assets/img/youtube.png'
                elif icon == 'Twitter':
                    image = 'base/assets/img/tw.png'
                elif icon == 'Instagram':
                    image = 'base/assets/img/in.png'
                elif icon == 'Linkedin':
                    image = 'base/assets/img/linked.png'
                elif icon == 'Tik Tok':
                    image = 'base/assets/img/tic.png'
                elif icon == 'DropBox':
                    image = 'base/assets/img/dp.png'
                elif icon == 'Pinterest':
                    image = 'base/assets/img/pinterest.png'
                elif icon == 'NGL':
                    image = 'base/assets/img/ngl.png'
                elif icon == 'Discord':
                    image = 'base/assets/img/discord.png'
                elif icon == 'OnlyFans':
                    image = 'base/assets/img/onlyfans.png'
                profile = Profile.objects.get(user=request.user)
                Linksmedia.objects.create(user=request.user,
                                          title=title, url=url, icon=icon, image=image, profile=profile)
            return render(request, 'home/index.html', context)
    else:
        return redirect('/')


def search(request):
    if request.user.is_authenticated:
        check_profrile = Profile.objects.filter(user=request.user).exists()
        if check_profrile:
            obj = Linksmedia.objects.order_by('-id')
            profile = Profile.objects.get(user=request.user)
            friends = profile.friends.all()
            # for search
            search_ = request.GET['query']
            profiles = Profile.objects.filter(
                user__username__icontains=search_)
            # end search
            context = {
                'links': LinksmediaForm,
                'posts': obj,
                'profile': profile,
                'profiles': profiles,
                'username': search_,
                'profile_username': profile.user,
                'friend_list': friends
            }

            if request.method == "POST":
                title = request.POST.get('title')
                url = request.POST.get('url')
                icon = request.POST.get('icon')
                image = None

                if icon == 'Web Link':
                    image = 'base/assets/img/web.png'
                elif icon == 'Facebook':
                    image = 'base/assets/img/fb.png'
                elif icon == 'Youtube':
                    image = 'base/assets/img/youtube.png'
                elif icon == 'Twitter':
                    image = 'base/assets/img/tw.png'
                elif icon == 'Instagram':
                    image = 'base/assets/img/in.png'
                elif icon == 'Linkedin':
                    image = 'base/assets/img/linked.png'
                elif icon == 'Tik Tok':
                    image = 'base/assets/img/tic.png'
                elif icon == 'DropBox':
                    image = 'base/assets/img/dp.png'
                elif icon == 'Pinterest':
                    image = 'base/assets/img/pinterest.png'
                elif icon == 'NGL':
                    image = 'base/assets/img/ngl.png'
                elif icon == 'Discord':
                    image = 'base/assets/img/discord.png'
                elif icon == 'OnlyFans':
                    image = 'base/assets/img/onlyfans.png'

                Linksmedia.objects.create(
                    title=title, url=url, icon=icon, image=image)
            # for post end

            return render(request, 'home/search.html', context)
    else:
        return redirect('/')


def update_post(request, id):
    if request.method == 'POST':
        get_id = Linksmedia.objects.get(id=id)
        fm = LinksmediaForm(request.POST, request.FILES, instance=get_id)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            url = fm.cleaned_data['url']
            icon = fm.cleaned_data['icon']
            image = None
            if icon == 'Web Link':
                image = 'base/assets/img/web.png'
            elif icon == 'Facebook':
                image = 'base/assets/img/fb.png'
            elif icon == 'Youtube':
                image = 'base/assets/img/youtube.png'
            elif icon == 'Twitter':
                image = 'base/assets/img/tw.png'
            elif icon == 'Instagram':
                image = 'base/assets/img/in.png'
            elif icon == 'Linkedin':
                image = 'base/assets/img/linked.png'
            elif icon == 'Tik Tok':
                image = 'base/assets/img/tic.png'
            elif icon == 'DropBox':
                image = 'base/assets/img/dp.png'
            elif icon == 'Pinterest':
                image = 'base/assets/img/pinterest.png'
            elif icon == 'NGL':
                image = 'base/assets/img/ngl.png'
            elif icon == 'Discord':
                image = 'base/assets/img/discord.png'
            elif icon == 'OnlyFans':
                image = 'base/assets/img/onlyfans.png'
            instance = Linksmedia.objects.get(id=id)
            instance.title = title
            instance.url = url
            instance.icon = icon
            instance.image = image
            instance.save()
            return redirect('/feed')
    else:
        get_id = Linksmedia.objects.get(id=id)
        fm = LinksmediaForm(instance=get_id)
    return render(request, 'home/update.html', {'links': fm})


def delete(request):
    data = request.POST
    id = data.get('id')
    print(id)
    post = Linksmedia.objects.get(id=id)
    post.delete()
    return redirect('/feed')


def friends(request, id, username):
    profile = Profile.objects.get(id=id)
    login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.friends.all():
        profile.friends.remove(request.user)
        login_profile.friends.remove(profile.user)
    else:
        profile.friends.add(request.user)
        login_profile.friends.add(profile.user)
    return redirect(f'/feed/search?query={username}')
