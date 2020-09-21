$( document ).ready(function() {
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $('#btn-user-next').click(function(event) {
        data_dict = {
            'username' : $('#userID').val()
        }


        $.get('submit_user_form/',data_dict, function(data){
            window.location.href = data['redirect-url']
        });

     });

    $("#button1").click( function()
       {
            var q1 = $("input:radio[name ='q1']:checked").val();

            var q2 = $("input:radio[name ='q2']:checked").val();

            var q3 = $("input:radio[name ='q3']:checked").val();


            if( typeof q1 === "undefined"){
                alert("Please answer the first question");
                return;
            }
            if( typeof q2 === "undefined"){
                alert("Please answer the second question");
                return;
            }
            if( typeof q3 === "undefined"){
                alert("Please answer the third question");
                return;
            }

            $.ajax({
                type: 'POST',
                url: 'save_pre_survey',
                data: {
                    'q1' : q1 ,
                    'q2' : q2 ,
                    'q3' : q3
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });


       }
    );

    $("#mental_model_btn").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#button_session_1").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
             $.ajax({
                 type: 'POST',
                 url: 'save_session_1',
                 data: {
                     'response' : result
                 },
                 success: function(data){
                     if (data['status'] == 1){
                         window.location.href = data['redirect-url']
                     }
                 }
             });
       }
    );

    $("#session_2_button").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_session_2',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#button_post_survey").click( function()
       {
            var q1 = $("input:radio[name ='q1']:checked").val();

            var q2 = $("input:radio[name ='q2']:checked").val();

            var q3 = $("input:radio[name ='q3']:checked").val();


            if( typeof q1 === "undefined"){
                alert("Please answer the first question");
                return;
            }
            if( typeof q2 === "undefined"){
                alert("Please answer the second question");
                return;
            }
            if( typeof q3 === "undefined"){
                alert("Please answer the third question");
                return;
            }

            $.ajax({
                type: 'POST',
                url: 'save_post_survey',
                data: {
                    'q1' : q1 ,
                    'q2' : q2 ,
                    'q3' : q3
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });


       }
    );

    $("#mental_model_btn_1").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model_1',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#mental_model_btn_2").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model_2',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#mental_model_btn_3").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model_3',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#mental_model_btn_4").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model_4',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );

    $("#mental_model_btn_5").click( function()
       {
            var checked_radio_list = $("input[type='radio']:checked");
            var unchecked_radio_list = $("input[type='radio']:not(:checked)");

            if( unchecked_radio_list.length > 0 ){
//                alert("Please make sure to respond to each book.")
//                return;
            }

            var result = '';
            $.each( checked_radio_list , function(index, value){
                result = value.name + '-' + value.id +  '-' + $(value).data( "isbn" ) + ';' + result ;
            });
            console.log(result)
            $.ajax({
                type: 'POST',
                url: 'save_mental_model_5',
                data: {
                    'response' : result
                },
                success: function(data){
                    if (data['status'] == 1){
                        window.location.href = data['redirect-url']
                    }
                }
            });
       }
    );


     $('[id*="load_more_link"]').click( function()
       {
            var isbn = this.id.split('-')[1]
            $.ajax({
                type: 'POST',
                url: 'get_book_details',
                data: {
                    'ISBN' : isbn
                },
                success: function(data){
                    $("#modal_holder" ).html(data);

                    $('#book_details_modal').modal('toggle');

                    console.log(data)
//                    if (data['status'] == 1){
//                        console.log(data)
//                        console.log(data['book_details'])
//                    }
                }
            });

       }
    );

});