function toggleSearch() {
    var popup = document.getElementById("searchFormPopup");
    if (popup.style.display === "none") {
         popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
}


$(document).ready(function() {
    $('.edit-button').click(function() {
        var infoId = $(this).data('id');
        $('#info-item-' + infoId).hide();
        $('#edit-form-' + infoId).show();
    });

    $('.edit-form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var infoId = form.attr('id').split('-')[2];
        var formData = form.serialize();

        $.ajax({
            url: "/update/" + infoId + "/",  
            type: "POST",
            data: formData,
            success: function(response) {
                if (response.success) {
                    var newUsername = response.data.username;
                    var newEmail = response.data.email;
                    var newNumber = response.data.number;
                    var newTimeUpdate = response.data.time_update;

                    $('#info-item-' + infoId + ' h2').text(newUsername);
                    $('#info-item-' + infoId + ' .email').text('Почта: ' + newEmail);
                    $('#info-item-' + infoId + ' .number').text('Номер: ' + newNumber);
                    $('#info-item-' + infoId + ' .time_update').text('Последнее редактирование: ' + newTimeUpdate);

                    $('#edit-form-' + infoId).hide();
                    $('#info-item-' + infoId).show();
                } else {
                    alert('Не удалось обновить данные');
                }
            },
            error: function() {
                alert('Произошла ошибка при обновлении данных');
            }
        });
    });
});



$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('.delete-button').click(function() {
        var infoId = $(this).data('id');
        if (confirm('Вы уверены, что хотите удалить эту запись?')) { 
            $.ajax({
                url: '/delete/' + infoId + '/',
                type: 'DELETE',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                },
                dataType: 'json',
                success: function(response) {
                    if (response.success) {
                        $('#info-item-' + infoId).remove();  
                    } else {
                        alert('Ошибка при удалении записи: ' + response.error);
                    }
                },
                error: function(xhr, status, error) {
                    alert('Произошла ошибка при удалении: ' + error);
                }
            });
        }
    });
});