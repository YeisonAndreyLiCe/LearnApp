
$(window).ready(function() {
    /* var form = document.getElementById(id); */
    var form 
    var fetchTo
    function findId(id){
        form = document.getElementById(id);
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
                    alert(data.enroll_course);
                }
            });
        };
    };
});