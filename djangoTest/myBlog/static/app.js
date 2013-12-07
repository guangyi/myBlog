'use strict';

var Blog = angular.module("Blog",["ngCookies"], function($interpolateProvider){
	$interpolateProvider.startSymbol("{$");
	$interpolateProvider.endSymbol("$}");
});

Blog.run(function($http, $cookies){
	$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

Blog.config(function ($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: "/templates/myBlog/post_list.html", 
			controller: "postCtrl",
			resolve:{
				posts:function(PostService){
					return PostService.list();
				}
			} 
		})
		.otherwise({
			redirectTo:'/'
		})
});