/*var appController = Blog.controller('appController', function($scope,$rootScope,$location,$GlobalService){
	var failureCb = function(status){
		console.log(status);
	};
	$scope.globals = GlobalService;
	$scope.initialize = function(is_authenticated){
		$scope.gloables.is_authenticated = is_authenticated;
	}
});*/
Blog.controller('postCtrl', function($scope,PostService,$http){
	//$scope.posts = posts;
	//$scope.globals = GlobalService;
	$http({
		method:'GET',
		url:'/'
	}).success(function(data,status,hearders,config){
		$scope.posts = data;
	})
	$scope.open = function(action){
		if(action ==='create'){
			$scope.postModalCreate = true;
			$scope.post = new Object();
		};
	};
	$scope.create = function(){
		$http({
			//post can't get return data?
			method:'POST',
			url:'/',
			data:$scope.post
		}).success(function(data,status,headers,config){
			$scope.posts.push(data);
			$scope.post = {};
		})

		/*
		PostService.save($scope.post).then(function(data){
			$scope.post = data;
			$scope.posts.push(data);
			$scope.postModalCreate = false;
		}, function(status){
			console.log(status);
		});*/
	};
});