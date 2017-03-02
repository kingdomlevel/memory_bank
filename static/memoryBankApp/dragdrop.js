$( init );
 
function init() {
	$('#listContainer').draggable( {
		containment: 'parent',
		cursor: 'move',
		snap: '#listBoard'
	});
}
