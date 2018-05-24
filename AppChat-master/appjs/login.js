angular.module('AppChat').$controller('LoginController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope, $location) {
        
        var thisCtrl = this;
        
        this.signUpRedirect = function(){
        $scope.nowdate = Date();
           $location.url('/signup');
        };
        
        
        
        this.signUpRedirect();
}]);
