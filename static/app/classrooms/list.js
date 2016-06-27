'use strict';

var module_movies = angular.module('myApp.classrooms', ['ngRoute', 'ngSanitize', 'ClassroomService']);

module_movies.controller('ClassroomController',
    ['$scope', '$routeParams', '$sce', 'ClassroomService',
    function($scope, $routeParams, $sce, classroomService) {

        $scope.classrooms = [];
        $scope.showDetails = function(classroom){
                showClassroom(classroom);
            };

        classroomService.getClassrooms()
            .then(function(data) {
                // SUCCESS
                processData(data);
            })
            .catch(function(error) {
                // ERROR
                console.error(error);
            });

        function processData(data){
            $scope.classrooms = data;
            if( $routeParams.classroomId ){
                $scope.classroomId = $routeParams.classroomId;
                $scope.selectedClassroom = getClassroom($routeParams.classroomId);
                $scope.showClassroom = Boolean($scope.selectedClassroom);
            }
            else{
                $scope.classroomId = '';
                $scope.selectedClassroom = null;
                $scope.showClassroom = false;
            }
        }

        function showClassroom(classroom){
            if(classroom){
                $scope.selectedClassroom = classroom;
                $scope.classroomId = classroom.id;
                $scope.showClassroom = Boolean($scope.selectedClassroom);
            }
        }

        function getClassroom(classroomId){
            if( $scope.classrooms ){
                for(var i=0; i<$scope.classrooms.length; i++){
                    var classroom = $scope.classrooms[i];
                    if( classroom.id == classroomId ){
                        return classroom;
                    }
                }
            }
            return null;
        }
    }]);



var module_movies_service = angular.module('ClassroomService', ['ngResource']);
module_movies_service.service( "ClassroomService",
    function( $http, $q ) {

        // ------------------------------- PUBLIC API
        return({
            getClassrooms: getClassrooms        // returns a promise
        });



        // --------------------------------------------------------------------
        function getClassrooms() {
            var request = $http({
                method: "get",
                url: "/classrooms",
                params: {
                    action: "get"
                }
            });
            return( request.then(handleSuccess, handleError) );
        }

        function handleSuccess(response) {
            return( response.data );
        }

        function handleError(response) {
            if ( !angular.isObject(response.data) || !response.data.message ) {
                return( $q.reject("An unknown error occurred.") );
            }
            return( $q.reject(response.data.message) );
        }
    });
