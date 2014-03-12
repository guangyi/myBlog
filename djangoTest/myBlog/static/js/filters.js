Blog.filter('Edit', function(){
	return function(editing){
		if (editing == true){
			return 'Cancel';
		}
		else return 'Edit';
	}
})