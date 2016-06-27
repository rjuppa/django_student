'use strict';

var myApp = angular.module('myApp', [
  'ngRoute',
  'ngSanitize',
  'myApp.classrooms',
  'myApp.about'
]);


myApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/classrooms', {
            templateUrl: '/static/app/classrooms/list.html',
            controller: 'ClassroomController'
        });
        $routeProvider.when('/classrooms/:classroomId', {
            templateUrl: '/static/app/classrooms/list.html',
            controller: 'ClassroomController'
        });
        $routeProvider.when('/about', {
            templateUrl: '/static/app/about/about.html',
            controller: 'AboutCtrl'
        });
        $routeProvider.otherwise({redirectTo: '/about'});
    }]);
