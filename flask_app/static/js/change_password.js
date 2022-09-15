$(document).ready(function() {
    $('#change_password_button').click(function() {
        change = `<label for="password">New Password</label>
                                                <input type="password" class="form-control" id="password" name="password">
                                                <label for="confirmPassword">Confirm New Password</label>
                                                <input type="password" class="form-control" id="confirmPassword" name="confirm_password">`;
        $("#change_password").html(change);
        var form = document.getElementById('form');
        var FetchTo = form.getAttribute('action');
        form.onsubmit = function(e) {
            e.preventDefault();
            var formData = new FormData(form);
            fetch(FetchTo,{'method': 'POST', 'body': formData})
            .then (response => response.json())
            .then (data => {
                if ('route' in data) {
                    window.location.href = data.route;
                }
                else {
                    var alertMessage = document.getElementById('alertMessage');
                    alertMessage.innerHTML = "";
                    for (var key in data) {
                        alertMessage.innerHTML += data[key] + '<br>';
                    }
                    //alertMessage.innerText = data.error;
                    alertMessage.classList.add('alert');
                    alertMessage.classList.add('alert-danger');
                }
            });
        }
    });
});