'use strict';   

var convertOrders = angular.module('convertOrders', [
 'ngRoute',
 'ngCookies',
 'convertControllers',
 'convertServices',
 'ui.bootstrap',
 'ui.bootstrap.tpls'
]);

convertOrders.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '../static/partials/home.html'
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html'
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);