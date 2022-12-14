function autoGrow(element){
    element.style.height = "5px";
    element.style.height = (element.scrollHeight)+"px";
    element.style.overflow = "hidden";
}
var data 
var select = ""
function getInfo(information) {
    data = eval(information);
    select = "";
    for(var i = 0; i < data.length; i++) {
        select += `<option value='${data[i].id}'> ${data[i].name}</option>`;
    };
};
$(document).ready(function() {
    form = $('#form');
    $('.list-group-item-info .nav-link').each(function(){
        $(this).click(function(){
            $(this).addClass('text-info');
            $(this).removeClass('text-dark');
            $(this).parent().siblings().children().removeClass('text-info');
            $(this).parent().siblings().children().addClass('text-dark');
        });
    });
    $('.list-group-item').each(function() {
        $(this).click(function() {
            $(this).addClass('active');
            $(this).siblings().removeClass('active');
            var id = $(this).attr('id');
            $('#title').html(id);
            var baseFields = `<div class="form-group my-3">
                            <label for="name">Name</label>
                            <input type="text" class="form-control" id="name" name="name">
                        </div>
                        <div class="form-group my-3">
                            <label for="description">Description</label>
                            <textarea class="form-control" id="description" name="description" rows="3" onkeydown="autoGrow(this)" onkeyup="autoGrow(this)"></textarea>
                        </div>`;
            var button = `<button type="submit" class="btn btn-primary">Submit</button>`;
            if(id == 'category') {
                var fields = `${baseFields} 
                            <div class="form-group my-3">
                                <label for="imageCategory">Category Image</label>
                                <input type="file" class="form-control" id="imageCategory" name="image">
                            </div> ${button}`;
                $('#form').html(fields);
                /* $('#form').attr('action', '/create_category'); */
            }
            else if(id == 'course') {
                var fields =`${baseFields} 
                            <div class="form-group my-3">
                                <label for="imageCourse">Course Image</label>
                                <input type="file" class="form-control" id="imageCourse" name="image">
                            </div>
                            <div class="form-group my-3">
                                <label for="courseInstructor">Instructor Email</label>
                                <input type="email" class="form-control" id="courseInstructor" name="instructor_email">
                            </div>
                            <div class="form-group my-3">
                                <label for="courseCategory">Category</label>
                                <select class="form-select" aria-label="Default select example" name="category_id"> 
                                    ${select}
                                </select>
                            </div>
                            ${button}`;
                $('#form').html(fields);
                /* $('#form').attr('action', '/create_course'); */
            }
            else if(id == 'record') {
                var fields = `<div class="form-group my-3">
                                <label for="name">Name</label>
                                <input type="text" class="form-control" id="name" name="name">
                            </div>
                            <div class="form-group my-3">
                                <label for="description">Description</label>
                                <textarea class="form-control" id="description" name="description" rows="3" onkeydown="autoGrow(this)" onkeyup="autoGrow(this)"></textarea>
                            </div>
                            <div class="form-group my-3">
                                <label for="recordCourse">Record Info</label>
                                <input type="file" class="form-control" id="recordCourse" name="record">
                            </div>
                            <div class="form-group my-3">
                                <label for="courseCategory">Courses</label>
                                <select class="form-select" aria-label="Default select example" name="course_id">`+
                                select
                                +`</select> </div>`+button;
                $('#form').html(fields);
                /* $('#form').attr('action', '/create_record'); */
                /* $('#form').attr('enctype', 'multipart/form-data'); */
            }
        });
    });
});