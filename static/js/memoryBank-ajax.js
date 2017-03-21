
$('#bankList').keyup(function(){
var query;
query = $(this).val();
$.get('memorybank/bankitems/', {suggestion: query},function(data){
$('#banklist').html(data);
 });
});