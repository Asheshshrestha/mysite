(function($) {
    $.SubscriberObj = function(p) {
        let $validator;
        var ManageNewSubscribe = {
            config: {
                async: false,
                cache: false,
                type: 'POST',
                data: '{}',
                methodname: '',
                baseURL: ''
            },

            init: function() {
                ManageNewSubscribe.initEvents();
            },
            initEvents: function() {
                $('#btnSubmit').off('click').on('click', function(e) {
                    if (!$validator.form()) {
                        e.preventDefault();
                    }
                });
            }

        }

        $validator = $('#formSubs').validate({
            rules: {
                Email: { required: true, email: true }
            },
            messages: {
                Username: { required: '* required', email: '* enter valid email' }

            },
            ignore: ':hidden, :disabled'
        });

        ManageNewSubscribe.init();
    };

    $.fn.ManageSubscribeFn = function(p) {
        $.SubscriberObj(p);
    };
})(jQuery);