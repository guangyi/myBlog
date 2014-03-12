Blog.factory('PostService', function($http, $q){
	var api_url = "posts/";
	return {
		get:function(postID){
			var url = api_url + postID + '/';
			var defer = $q.defer();
			$http({
				method:'GET',
				url: url
			}).success(function(data, status, headers, config){
				defer.resolve(data);
			}).error(function(data, status, headers, config){
				defer.reject(status);
			});
			return defer.promise;
		},
		save: function(post) {
			var url = api_url;
			var defer = $q.defer();
			$http({
				method:'POST',
				url:url,
				data: post
			}).success(function(data, status, headers, config){
				defer.resolve(data);
			}).error(function(data, status, headers, config){
				defer.reject(status);
			});
			return defer.promise;
		},
		list:function(){
			var defer = $q.defer();
			$http({
				method:'GET',
				url:api_url})
			.success(function(data, status, headers, config){
				defer.resolve(data);
			}).error(function(data, status, headers, config){
				defer.reject(status);
			});
			return defer.promise;
		},
		update:function(postID, post){
			var url = api_url + postID + '/';
			var defer = $q.defer();
			console.log(url)
			$http({
				method:'PUT',
				url:url,
				data: post
			})
			.success(function(data, status, headers, config){
				defer.resolve(data);
			}).error(function(data, status, headers, config){
				defer.reject(status);
			});
			return defer.promise;
		},
		delete:function(postID, post){
			var url = api_url + postID + '/';
			var defer = $q.defer();
			$http({
				method:'DELETE',
				url:url,
				data:post
			}).success(function(data, status, headers, config){
				defer.resolve('success');
			}).error(function(data, status,headers,config){
				defer.reject(status);
			});
			return defer.promise;
		}
	}
});
Blog.factory('UserService',function($http, $q){
	var user_url = 'user/';
	return{
		userList:function(){
			var defer = $q.defer();
			$http({
				method:'GET',
				url:user_url
			}).success(function(data, status, headers,config){
				defer.resolve(data);
			}).error(function(data, status,headers,config){
				defer.reject(status);
			});
			return defer.promise;
		}
	}
});

/*
Blog.factory('Post',['$resource', function($resource){
	$resource('/lists/'); 
}]);*/