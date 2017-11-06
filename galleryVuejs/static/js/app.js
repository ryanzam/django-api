$(document).ready(function () {

    var root = "http://localhost:8000/api/images/"

    $.ajax({
        url: root,
        dataType: 'json'
    }).done(function (data) {
        $.map(data, function (img, i) {
            $('#img-gal').append('<img src="'+img.thumbnail+'"/>')
        })
    })
});