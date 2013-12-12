Blog.factory('PostService', function($http, $q){
	var api_url = "posts/";
	return {
		get:function(postID){
			var url = api_url + postID + '/';
			var defer = $q.defer();
			$http({method:'GET',
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
		}
	}
});
/*
Blog.factory('Post',['$resource', function($resource){
	$resource('/lists/'); 
}]);*/