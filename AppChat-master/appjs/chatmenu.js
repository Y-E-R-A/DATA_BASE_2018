/**
 * Created by manuel on 4/24/18.
 */
angular.module('AppChat').controller('ChatMenuController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object
        var thisCtrl = this;
        
        this.contactChatsRedirect = function(){
            $location.url('/group/'+ $routeParams.uid);  
        }
        
        
        this.GroupRedirect = function(){
            $location.url('/group/'+ $routeParams.uid);
        }
        
        
}]);