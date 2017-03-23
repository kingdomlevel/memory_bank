// Copies the list ID to to the list item form.
$(document).ready(function() {
    $('.listButton').click(function(e) {
        target = $(e.target);
        title = target.attr('data-title');
        id = target.attr('data-id');
        $('#addItemTitle').text('Add item to "' + title+'"');
        $('#newItemListID').val(id);

    });
});

// Copies text from the editor on the edit enhanced list
// page to a form field that saves to the database.
$(document).ready(function() {
    text = $('#id_long_text');
    $('#editor1').val(text.val());
    $('#hiddentext').hide();
});


// triggered by the 'x' in the listboxes and sets
// a boolean field to true so that it no longer
// appears on the home page.
$(document).ready(function() {
    $('.deleteList').click(function(e) {
        target = $(e.target);
        title = target.attr('data-title');
        id = target.attr('data-id');
        $('#deleteItemTitle').text('Are you sure you want to delete "' + title+'"');
        $('#DeleteListID').val(id);
        $('#DeleteListBool').val('1');
    });
});

// Redirects back to home if the user clicks
// the cancel button
$(document).ready(function() {
      $('.cancelEdit').click(function() {
      window.location.href = "/memorybank/home";
      });
  });

  // Redirects back to enhancedlist if the user clicks
  // the cancel button
  $(document).ready(function() {
        $('.cancelEnhancedEdit').click(function() {
        window.location.href = "/memorybank/enhancedlist";
        });
    });

// Redirects back to home if the user clicks
// the cancel button
$(document).ready(function() {
      $('.cancelDelete').click(function() {
      window.location.href = "/memorybank/home";
      });
  });

// Confirms the delete for the list
$(document).ready(function() {
    $('.submitDelete').click(function() {
        if (confirm("Are you sure you want to delete this item?")){
          $('#removeFormField').val('1');
          document.getElementById("ListForm").submit();
        }
    });
});

//takes a value from the bank select tag and moves it to title input.
function OnDropDownChange(dropDown) {
    var selectedValue = dropDown.options[dropDown.selectedIndex].value;
    document.getElementById("banktitle").value = selectedValue;}


//when user clicks the list item title input, the bank <div> fades out
$(document).ready(function() {
    $("#banktitle").click(function(){
        $("#banker").fadeOut("slow", function(){
        });
    });
});


//when user unfocuses the list title box the bank <div> fades in , ONLY if an empty string is present in the input
$(document).ready(function() {
    $("#banktitle").blur(function()
    {
       if(!$(this).val()){
        $("#banker").fadeIn("slow");
        }
    });
});
