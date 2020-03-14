const baseUrl = 'http://localhost:8000/api/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function makeRequest(path, method, auth = true, data = null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'Authorization': 'Token ' + getToken()};
    }
    return $.ajax(settings);
}

function saveToken(token) {
    localStorage.setItem('authToken', token);
}

function getToken() {
    return localStorage.getItem('authToken');
}

function removeToken() {
    localStorage.removeItem('authToken');
}

function logIn(username, password) {
    const credentials = {username, password};
    let request = makeRequest('login', 'post', false, credentials);
    request.done(function (data, status, response) {
        console.log('Received token');
        saveToken(data.token);
    }).fail(function (response, status, message) {
        console.log('Could not get token');
        console.log(response);
    });
}

$(document).ready(function () {
    let token = getToken();
    if (!token) logIn('admin', 'admin');
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function privatesAddSuccess(data) {
    console.log(data);
    let filePk = data.pk;
    $('#add-to-privates-' + filePk).addClass('d-none');
    $('#delete-from-privates-' + filePk).removeClass('d-none');
}

function privatesDeleteSuccess(data) {
    console.log(data);
    let filePk = data.pk;
    $('#add-to-privates' + filePk).removeClass('d-none');
    $('#delete-from-privates' + filePk).addClass('d-none');
}

function privatesAdd(e) {
    e.preventDefault();
    let link = $(e.target);
    let href = link.attr('href');
    let file_pk = link.data('file-pk');
    $.ajax({
        method: 'post',
        url: href,
        data: {'pk': file_pk},
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .done(privatesAddSuccess)
        .fail(console.log);
}

function privateselete(e) {
    e.preventDefault();
    let link = $(e.target);
    let href = link.attr('href');
    let file_pk = link.data('file-pk');
    $.ajax({
        method: 'post',
        url: href,
        data: {'pk': file_pk},
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .done(privatesDeleteSuccess)
        .fail(console.log);
}

function setUpPrivateButtons() {
    $('.privates-add').click(privatesAdd);
    $('.privaes-delete').click(privatesDelete);
}

$(document).ready(setUpPrivateButtons);
