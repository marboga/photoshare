(function () {
    'use strict';

    angular
        .module('photocollection.user.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Authentication'];


    function LoginController($location, $scope, Authentication) {
        var vm = this;

        vm.login = login;

        activate();

        function activate() {
            // if the user is authenticated, they should not be here.
            if(Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }

        function login() {
            Authentication.login(vm.email, vm.password);
        }
    }
})();