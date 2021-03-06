var appController = Blog.controller('appController', function($scope,$rootScope,$location,GlobalService){
	var failureCb = function(status){
		console.log(status);
	};
	$scope.globals = GlobalService;
	$scope.initialize = function(is_authenticated){
		$scope.gloables.is_authenticated = is_authenticated;
	}
});
Blog.controller('postCtrl', function($scope,PostService,posts,$http, $location){
	//$scope.posts = posts;
	//$scope.globals = GlobalService;
	/*$http({
		method:'GET',
		url:'/'
	}).success(function(data,status,hearders,config){
		$scope.posts = data;
	})*/
$scope.limits = 300;
$scope.show = false;
	$scope.posts = posts;
	if ($scope.posts == []){
		$scope.posts = '';
	}
	$scope.open = function(action){
		if(action ==='create'){
			$scope.postModalCreate = true;
			$scope.post = new Object();
		};
	};
	$scope.create = function(){
		PostService.save($scope.post).then(function(data){
			$scope.show = true;
			$scope.msg = "✓Your blog has been published successfully!";
			$scope.post = data;
			$scope.posts.push(data);
		}, function(reason){
			$scope.show = true;
			$scope.msg = "Oops! Error. blog not published, try again!"
		},function(update){
		}).then(function(data){
			$location.path('/');
		});
	};
});
Blog.controller('userCtrl',function($scope, UserService, users){
	$scope.users = users;
})
Blog.controller('detailCtrl',function($scope,PostService, post, $http, $route,$location){
	//scope.post and newPost all point to post object
	//when editing post, actually it's editing post object
	//so newPost will change with scope.post
	//$scope.post = post;
	//$scope.newPost = post;
	var copyPost = function(post, newPost){
		//this function is to copy content from post to newPost or opposite way
		newPost.title = post.title;
		newPost.description = post.description;
	}
	var postID = $route.current.params.id;
	$scope.post = post;
	$scope.newPost = {};
	$scope.editing = false;
	copyPost($scope.post, $scope.newPost);
	
	$scope.editOrCancel = function(){
		//
		$scope.editing = ! $scope.editing;
		//if click Cancel:
		if ($scope.editing == false){
			copyPost($scope.post, $scope.newPost);
		}
	}
	$scope.save = function(){
		// solved but why? why can not 
		copyPost($scope.newPost, $scope.post);
		PostService.update(postID, $scope.post);
		$scope.editing = false;
		//$scope.post = post;
	};
	$scope.delete = function(){
		PostService.delete(postID, $scope.post);
			console.log('here');
			$location.path('/');
	};
});