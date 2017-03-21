
$(document).ready(function() {
    $('.listButton').click(function(e) {
        target = $(e.target);
        title = target.attr('data-title');
        id = target.attr('data-id');
        $('#addItemTitle').text('Add item to "' + title+'"');
        $('#newItemListID').val(id);

    });
});


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


$('AddListForm').submit(function(){
    alert(title);
    target = $(e.target);
    title = target.attr('data-title');
});


$(document).ready(function(){
  $('.submitAddList').submit(function(){
      doc = document.getElementById("AddListForm")
      target = $(e.target);
      title = target.attr('data-title');
      alert(doc.title);

  });
});

$(document).ready(function() {
      $('.cancelEdit').click(function() {
      window.location.href = "/memorybank/home";       
      });
  });


$(document).ready(function() {
      $('.cancelDelete').click(function() {
      window.location.href = "/memorybank/home";       
      });
  });


$(document).ready(function() {
    $('.submitDelete').click(function() {
        if (confirm("Are you sure you want to delete this item?")){
          $('#removeFormField').val('1');        
          document.getElementById("ListForm").submit();
        }
                    
    });
});


//  $( function() {
//    $.widget( "custom.combobox", {
//      _create: function() {
//        this.wrapper = $( "<span>" )
//          .addClass( "custom-combobox" )
//          .insertAfter( this.element );
//
//        this.element.hide();
//        this._createAutocomplete();
//        this._createShowAllButton();
//      },
//
//      _createAutocomplete: function() {
//        var selected = this.element.children( ":selected" ),
//          value = selected.val() ? selected.text() : "";
//
//        this.input = $( "<input>" )
//          .appendTo( this.wrapper )
//          .val( value )
//          .attr( "title", "" )
//          .addClass( "custom-combobox-input ui-widget ui-widget-content ui-state-default ui-corner-left" )
//          .autocomplete({
//            delay: 0,
//            minLength: 0,
//            source: $.proxy( this, "_source" )
//          })
//          .tooltip({
//            classes: {
//              "ui-tooltip": "ui-state-highlight"
//            }
//          });
//
//        this._on( this.input, {
//          autocompleteselect: function( event, ui ) {
//            ui.item.option.selected = true;
//            this._trigger( "select", event, {
//              item: ui.item.option
//            });
//          },
//
//          autocompletechange: "_removeIfInvalid"
//        });
//      },
//
//      _createShowAllButton: function() {
//        var input = this.input,
//          wasOpen = false;
//
//        $( "<a>" )
//          .attr( "tabIndex", -1 )
//          .attr( "title", "Show All Items" )
//          .tooltip()
//          .appendTo( this.wrapper )
//          .button({
//            icons: {
//              primary: "ui-icon-triangle-1-s"
//            },
//            text: false
//          })
//          .removeClass( "ui-corner-all" )
//          .addClass( "custom-combobox-toggle ui-corner-right" )
//          .on( "mousedown", function() {
//            wasOpen = input.autocomplete( "widget" ).is( ":visible" );
//          })
//          .on( "click", function() {
//            input.trigger( "focus" );
//
//            // Close if already visible
//            if ( wasOpen ) {
//              return;
//            }
//
//            // Pass empty string as value to search for, displaying all results
//            input.autocomplete( "search", "" );
//          });
//      },
//
//      _source: function( request, response ) {
//        var matcher = new RegExp( $.ui.autocomplete.escapeRegex(request.term), "i" );
//        response( this.element.children( "option" ).map(function() {
//          var text = $( this ).text();
//          if ( this.value && ( !request.term || matcher.test(text) ) )
//            return {
//              label: text,
//              value: text,
//              option: this
//            };
//        }) );
//      },
//
//      _removeIfInvalid: function( event, ui ) {
//
//        // Selected an item, nothing to do
//        if ( ui.item ) {
//          return;
//        }
//
//        // Search for a match (case-insensitive)
//        var value = this.input.val(),
//          valueLowerCase = value.toLowerCase(),
//          valid = false;
//        this.element.children( "option" ).each(function() {
//          if ( $( this ).text().toLowerCase() === valueLowerCase ) {
//            this.selected = valid = true;
//            return false;
//          }
//        });
//
//        // Found a match, nothing to do
//        if ( valid ) {
//          return;
//        }
//
//        // Remove invalid value
//        this.input
//          .val( "" )
//          .attr( "title", value + " didn't match any item" )
//          .tooltip( "open" );
//        this.element.val( "" );
//        this._delay(function() {
//          this.input.tooltip( "close" ).attr( "title", "" );
//        }, 2500 );
//        this.input.autocomplete( "instance" ).term = "";
//      },
//
//      _destroy: function() {
//        this.wrapper.remove();
//        this.element.show();
//      }
//    });
//
//    $( "#combobox" ).combobox();
//    $( "#toggle" ).on( "click", function() {
//      $( "#combobox" ).toggle();
//    });
//  } );






// </script>

/*<script type="text/javascript">
    $(document).ready(function(){
        $('.editButton').click(function(e) {
        target = $(e.target);
        title = target.attr('item-title');
        notes = target.attr('item-notes');

        $('#editItem').text('make changes to: "' + title + '"');
        $('#editItemNotes').text(''+ notes);

        });
    });

</script>*/
