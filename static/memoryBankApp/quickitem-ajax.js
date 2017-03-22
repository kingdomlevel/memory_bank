// AJAX for posting
function create_post(form) {
    console.log("create post is working!") // sanity check
    var list_id = $(form).closest("div").prop("id");
    //var title = $('#item-title').val()
    //var input = $("form input[id=id_title]");
    var list_el_id = "#" + list_id;
    console.log("list el id" + list_el_id);
    var input = $(list_el_id).find("#id_title");
    //var input = $(form).elements.namedItem('id_title')
    var title = (input).val();
    console.log(form);
    //var formData = $(form).serialize()
    //var formData = new FormData((form))
    console.log("form data:" + title);
    $.ajax({
        url : "/memorybank/quick_item/", // the endpoint
        type : "POST", // http method
        // processData: false,
        // contentType: false,
        data : { title : title, list_id : list_id }, // data sent with the post request
        //data : {title : title },

        // handle a successful response
        success : function(json) {
            $(input).val(''); // remove the value from the input
            $(input).focus(); // focus back onto the text field
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            $(list_el_id).load("/memorybank/update_list/", {'list_id' : list_id});
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// Submit post on submit
$('.quick_item_form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    //console.log(event.target.id)    // sanity check
    create_post(event.target);
});

// AJAX CSRF
$(function() {

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
