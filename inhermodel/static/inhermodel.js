$ = django.jQuery;

var form_name = "toplevel";

function level_one_manager(anc_name, is_enabled)
{
    var full_name, rel_name = "level_one";

    full_name = (anc_name.length > 0 ? anc_name + "-0-" : "" ) + rel_name;

    if (is_enabled) {
        $( "div[id='"+full_name+"-group'][.class='inline-group']" ).css('display', '');
    }
    else {
        $( "div[id='"+full_name+"-group'][.class='inline-group']" ).css('display', 'none');
    }
    related_delete_mgr(full_name, !is_enabled);
    // sub_manager(full_name, is_enabled) ....
}

function level_one_bi_manager(anc_name, is_enabled)
{
    var full_name, rel_name = "level_one_bi";

    full_name = (anc_name.length > 0 ? anc_name + "-0-" : "" ) + rel_name;

    if (is_enabled) {
        $( "div[id='"+full_name+"-group'][.class='inline-group']" ).css('display', '');
    }
    else {
        $( "div[id='"+full_name+"-group'][.class='inline-group']" ).css('display', 'none');
    }    
    related_delete_mgr(full_name, !is_enabled);
}

function related_delete_mgr(full_name, to_del)
{
    var el = $("#"+form_name+"_form input[id='id_"+full_name+"-0-DELETE']");

    // console.log("#"+form_name+"_form input[id='id_"+full_name+"-0-DELETE'], to_del="+(to_del ? "true" : "false"));
    if (el.length == 1) {
        if (to_del) {
            el.attr('checked','checked');
        }
        else {
            el.removeAttr('checked');
        }
    }
}


function top_level_manager(is_enabled) {
    var choice;

    choice = $( "#"+form_name+"_form select[id=id_choice] option:selected" ).text();
    $( "#"+form_name+"_form select[id=id_choice]" ).change(function () { top_level_manager(true) });

    level_one_manager("", choice == "Hindcasting");
    level_one_bi_manager("", choice == "Cross validation");
}

$(document).ready(function() {
    top_level_manager(true);
});
