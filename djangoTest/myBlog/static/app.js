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
			templateUrl: 'static/partial_view/post_list.html', 
			controller: "postCtrl",
			resolve:{
				posts:function(PostService){
					return PostService.list();
				}
			} 
		})
		.when('/post/:id',{
			templateUrl: 'static/partial_view/detail.html',
			controller:"detailCtrl",
			resolve:{
				post:function($route, PostService){
					var postID = $route.current.params.id;
					return PostService.get(postID);
				}
			}
		})
		.otherwise({
			redirectTo:'/'
		})
});