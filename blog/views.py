"""Blog views."""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Post, GuestUser, Comment, Like
from .forms import RegisterForm, LoginForm, NewPostForm, CommentForm
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import datetime


MYSALT = 'qe=xn06phh#is79y7'


def authentication(parameters):
    """Validate if the users is logged in."""
    guid = parameters.COOKIES.get('GUID')
    guid_sec = parameters.COOKIES.get('GUID-Secure')

    return check_password(guid, guid_sec)


# Create your views here.
def index(request):
    """URL: blog/ ."""
    template = loader.get_template('blog/index.html')
    latest_blog_list = Post.objects.filter(PostVisible=True) \
        .order_by('-PostDate')
    guid = 0
    if authentication(request):
        guid = int(request.COOKIES.get('GUID'))

    context = {
        'authentication': authentication(request),
        'latest_blog_list': latest_blog_list,
        'guid': guid,
    }
    return HttpResponse(template.render(context, request))


def new_post(request):
    """URL: blog/new/ ."""
    template = loader.get_template('blog/new_post.html')

    if not authentication(request):
        return HttpResponseRedirect('/blog/login/')

    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():

            save_new_post = Post(
                PostTitle=form.cleaned_data['PostTitle'],
                PostDate=datetime.datetime.now(),
                PostImageURL=form.cleaned_data['PostImageURL'],
                PostText=form.cleaned_data['PostText'],
                GuestUserKey_id=int(request.COOKIES.get('GUID')),
                PostVisible=form.cleaned_data['PostVisible'],
                )
            save_new_post.save()

            return HttpResponseRedirect('/blog/')

        else:
            context = {
                'authentication': authentication(request),
                'page_title': "New post",
                'form': form
            }
            return HttpResponse(template.render(context, request))

    else:
        form = NewPostForm()
        context = {
            'authentication': authentication(request),
            'page_title': "New post",
            'form': form
        }
        return HttpResponse(template.render(context, request))


def view_post(request, post_id):
    """URL: blog/(post_id) ."""
    template = loader.get_template('blog/post.html')
    this_post = Post.objects.get(pk=post_id)
    form = CommentForm()
    guid = 0
    if authentication(request):
        guid = int(request.COOKIES.get('GUID'))

    if this_post.GuestUserKey_id == guid:
        allow_edit = True
        allow_like = False
    else:
        allow_edit = False
        allow_like = True

    context = {
        'authentication': authentication(request),
        'allow_edit': allow_edit,
        'allow_like': allow_like,
        'this_post': this_post,
        'guid': guid,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def year_archive(request, year_var):
    """URL: blog/archive/(year)/ ."""
    template = loader.get_template('blog/year_archive.html')
    context = {
        'authentication': authentication(request),
    }
    return HttpResponse(template.render(context, request))


def month_archive(request, year_var, month_var):
    """URL: blog/archive/(year)/(month)/ ."""
    template = loader.get_template('blog/month_archive.html')
    context = {}
    return HttpResponse(template.render(context, request))


def day_archive(request, year_var, month_var, day_var):
    """URL: blog/archive/(year)/(month)/(day)/ ."""
    template = loader.get_template('blog/day_archive.html')
    context = {
        'authentication': authentication(request),
    }
    return HttpResponse(template.render(context, request))


def guest_register(request):
    """URL: blog/register/ ."""
    template = loader.get_template('blog/guest_register.html')
    context = {
        'authentication': authentication(request),
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            nohash_password = form.cleaned_data['Password']
            hash_password = make_password(
                nohash_password, salt=None, hasher='md5')

            register_new_user = GuestUser(
                FirstName=form.cleaned_data['FirstName'],
                LastName=form.cleaned_data['LastName'],
                Email=form.cleaned_data['Email'],
                Password=hash_password)
            register_new_user.save()

            return HttpResponseRedirect('/blog/login/')

        else:
            context = {
                'authentication': authentication(request),
                'form': form
            }
            return HttpResponse(template.render(context, request))

    else:
        form = RegisterForm()
        context = {
            'authentication': authentication(request),
            'form': form
        }
        return HttpResponse(template.render(context, request))


def guest_login(request):
    """URL: blog/login/ ."""
    template_name = 'blog/guest_login.html'
    template = loader.get_template(template_name)
    context = {
        'authentication': authentication(request),
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            """Open the session and split the view"""
            context = {
                'authentication': True,
            }

            email = form.cleaned_data['Email']
            remember_me = form.cleaned_data['RememberMe']
            model_ = GuestUser.objects.get(
                Email=email)

            if remember_me is True:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

            response = render(request, template_name, context)
            response.set_cookie('GUID', str(model_.pk))
            response.set_cookie('GUID-Secure', make_password(
                str(model_.pk), salt=MYSALT, hasher='md5'))

            return response

        else:
            context = {
                'authentication': authentication(request),
                'form': form
            }
            return HttpResponse(template.render(context, request))

    else:
        form = LoginForm()
        context = {
            'authentication': authentication(request),
            'form': form
        }
        return HttpResponse(template.render(context, request))


def guest_logout(request):
    """URL: blog/logout/ ."""
    template_name = 'blog/guest_logout.html'
    context = {
        'authentication': False,
    }
    response = render(request, template_name, context)
    response.set_cookie('GUID', '')
    response.set_cookie('GUID-Secure', '')
    return response


def comment_post(request, post_id):
    """URL: blog/(post_id)/comment/ ."""
    if not authentication(request):
        return HttpResponseRedirect('/blog/login/')

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():

            new_comment = Comment(
                CommentText=form.cleaned_data['CommentText'],
                CommentDate=datetime.datetime.now(),
                GuestUserKey_id=int(request.COOKIES.get('GUID')),
                PostKey_id=post_id
                )
            new_comment.save()

            return HttpResponseRedirect('/blog/'+post_id+'/#comments')

        else:
            return HttpResponseRedirect('/blog/'+post_id)

    else:
        return HttpResponseRedirect('/blog/'+post_id)


def comment_delete(request, post_id, comment_id):
        """URL: blog/(post_id)/comment/(comment_id) ."""
        if not authentication(request):
            return HttpResponseRedirect('/blog/login/')

        remove_comment = Comment.objects.get(pk=comment_id)
        if remove_comment.GuestUserKey_id == int(request.COOKIES.get('GUID')):
            remove_comment.delete()

        return HttpResponseRedirect('/blog/'+post_id+'/#comments')


def delete_post(request, post_id):
    """URL: blog/(post_id)/delete/ ."""
    if not authentication(request):
        return HttpResponseRedirect('/blog/login/')

    remove_post = Post.objects.get(pk=post_id)
    remove_post.delete()

    return HttpResponseRedirect('/blog/')


def edit_post(request, post_id):
    """URL: blog/(post_id)/edit/ ."""
    template = loader.get_template('blog/new_post.html')

    if not authentication(request):
        return HttpResponseRedirect('/blog/login/')

    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():

            update_post = Post.objects.get(pk=post_id)

            if update_post is not None:
                if update_post.GuestUserKey_id == int(request.COOKIES.get('GUID')):
                    update_post.PostTitle = form.cleaned_data['PostTitle']
                    update_post.PostImageURL = form.cleaned_data['PostImageURL']
                    update_post.PostText = form.cleaned_data['PostText']
                    update_post.PostVisible = form.cleaned_data['PostVisible']
                    update_post.save()

            return HttpResponseRedirect('/blog/')

        else:
            context = {
                'authentication': authentication(request),
                'page_title': "Edit post",
                'form': form
            }
            return HttpResponse(template.render(context, request))

    else:
        view_post = Post.objects.get(pk=post_id)
        form = NewPostForm(initial={
            'PostTitle': view_post.PostTitle,
            'PostImageURL': view_post.PostImageURL,
            'PostText': view_post.PostText,
            'PostVisible': view_post.PostVisible,
            })
        context = {
            'authentication': authentication(request),
            'page_title': "Edit post",
            'form': form
        }
        return HttpResponse(template.render(context, request))


def like_post(request, post_id):
    """URL: blog/(post_id)/like/ ."""
    if not authentication(request):
        return HttpResponseRedirect('/blog/login/')

    if post_id:

        guid = int(request.COOKIES.get('GUID'))
        isnotuser_post = Post.objects.get(pk=post_id)

        try:
            wasnotlikedbefore_post = Like.objects.get(
                PostKey_id=post_id,
                GuestUserKey_id=guid
                )
        except Exception as e:
            wasnotlikedbefore_post = None
        else:
            pass

        if isnotuser_post.GuestUserKey_id is not guid:
            if wasnotlikedbefore_post is None:
                try:
                    new_like = Like(
                        LikeDate=datetime.datetime.now(),
                        GuestUserKey_id=int(request.COOKIES.get('GUID')),
                        PostKey_id=post_id
                        )
                    new_like.save()
                except Exception as e:
                    return HttpResponseRedirect(
                        request.META.get('HTTP_REFERER')+'#postLike'+post_id)
                else:
                    return HttpResponseRedirect(
                        request.META.get('HTTP_REFERER')+'#postLike'+post_id)
            else:
                return HttpResponseRedirect(
                    request.META.get('HTTP_REFERER')+'#postLike'+post_id)
