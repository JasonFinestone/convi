'use strict';

var convertControllers = angular.module('convertControllers', []);


convertControllers.controller('convertCtrl', ['$scope', '$location', '$http', function($scope, $location, $http) {

console.log('Hello dude');

    $scope.getOrders = function() {

       console.log('Orders');

         $http({
            url: "/orders",
            method: "GET"
        }).success(function (data) {
            $scope.orders = data;
            console.log("Got list of orders", $scope.orders);
            $scope.processing = $scope.getFromCSV();

        }).error(function () {
            // Alert if login failed
            // alert("Error", data);
            console.log("Fail Got the following data from the server", data);
        });
    };


   $scope.getFromCSV = function() {

       console.log('Process');

         $http({
            url: "/process",
            method: "GET"
        }).success(function (data) {
            $scope.order = data;
            console.log("Got vtmf tags", $scope.order);
            $scope.fix = $scope.convertToFix();

        }).error(function () {
            // Alert if login failed
            // alert("Error", data);
            console.log("Fail Got the following data from the server", data);
        });
    };

    $scope.order_to_covert = {}

    $scope.convertToFix = function() {

        $scope.order_to_covert = $scope.order;

         console.log('Sending to be converted',$scope.order_to_covert);
         $http({
            url: "/process",
            method: "POST",
            data: $scope.order_to_covert
        }).success(function (data) {
            $scope.fix = data;
            console.log("Converted from vtmf to fix", $scope.fix);
             $scope.order = $scope.sendFix();
        }).error(function () {
            // Alert if login failed
            // alert("Error", data);
            console.log("Fail Got the following data from the server", data);
        });


    };

    $scope.order_to_send = {};

    $scope.sendFix = function() {

        $scope.order_to_send = $scope.fix;

         console.log('Sending this fix', $scope.order_to_send);
         $http({
            url: "/orders",
            method: "POST",
            data: $scope.order_to_send
        }).success(function (data) {
            $scope.sent = data;
            console.log("This is the response", $scope.sent);
        }).error(function () {
            // Alert if login failed
            // alert("Error", data);
            console.log("Fail Got the following data from the server", data);
        });


    };

}]);
