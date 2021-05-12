$('.openPopup').on('click', function () {
    var dataURL = $(this).attr('data-href');
    $('.modal-content').load(dataURL, function () {
        $('#modal-generico').modal({ show: true });
    });
});

$(document).on('hidden.bs.modal', function (e) {
var target = $(e.target);
target.removeData('bs.modal')
    .find(".modal-content").html('');
});