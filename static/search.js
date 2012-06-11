/**
 * Created with PyCharm.
 * User: caleb
 * Date: 4/21/12
 * Time: 6:53 PM
 * To change this template use File | Settings | File Templates.
 */
function search_submit() {
    var query = $("#id_query").val();
    $("#search-results").load(
        "/search_project/?ajax&query=" + encodeURIComponent(query)
    );
    return false;
}
$(document).ready(function () {
    $("#search-form").submit(search_submit);
});

