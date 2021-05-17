#Reference: https://github.com/MaksimEkin/COVID19-Literature-Clustering/blob/master/lib/call_backs.py
from bokeh.models import CustomJS

# handle the currently selected article
def selected_code():
    code = """
            var reviews = [];
            var isEdited = [];
            var reviewPostDate = [];
            var store = [];
            var ratings = [];
            var thumbsUps = [];
            var reviewAppVersion = [];
            var devResponseDate = [];
            var devResponse = [];

            cb_data.source.selected.indices.forEach(index => reviews.push(source.data["reviews"][index]));
            cb_data.source.selected.indices.forEach(index => isEdited.push(source.data["isEdited"][index]));
            cb_data.source.selected.indices.forEach(index => reviewPostDate.push(source.data["reviewPostDate"][index]));
            cb_data.source.selected.indices.forEach(index => store.push(source.data["store"][index]));
            cb_data.source.selected.indices.forEach(index => ratings.push(source.data["ratings"][index]));
            cb_data.source.selected.indices.forEach(index => thumbsUps.push(source.data["thumbsUp"][index]));
            cb_data.source.selected.indices.forEach(index => reviewAppVersion.push(source.data["reviewAppVersion"][index]));
            cb_data.source.selected.indices.forEach(index => devResponseDate.push(source.data["devResponseDate"][index]));
            cb_data.source.selected.indices.forEach(index => devResponse.push(source.data["devResponse"][index]));

            review = "<h4><b>Review: </b>" + reviews[0].toString() + "</h4>";
            reviewPostDate = "<p><b>Review post date: </b>" + reviewPostDate[0].toString() + "</p>"
            rating = "<p><b>Rating: </b> " + ratings[0].toString() + "</p>"
            thumbsUp =  "<p><b>Number of upvote: </b>" + thumbsUps[0].toString() + "</p>"
            store =  "<p><b>Store: </b>" + store[0].toString() + "</p>"
            devResponse = "<p><b>Dev response: </b>" + devResponse[0].toString() + "</p>"
            devResponseDate = "<p><b>Dev response date: </b>" + devResponseDate[0].toString() + "</p>"

            current_selection.text = review + reviewPostDate + rating + thumbsUp + store +devResponse + devResponseDate
            current_selection.change.emit();
    """
    return code

# handle the keywords and search
def input_callback(plot, source, out_text, topics): 

    # slider call back for cluster selection
    callback = CustomJS(args=dict(p=plot, source=source, out_text=out_text, topics=topics), code="""
				var key = text.value;
				key = key.toLowerCase();
				var cluster = slider.value;
                var data = source.data; 
                
                
                x = data['x'];
                y = data['y'];
                x_backup = data['x_backup'];
                y_backup = data['y_backup'];
                labels = data['desc'];
                reviews = data["reviews"];
                devResponse = data["devResponse"];
                if (cluster == '10') {
                    out_text.text = 'Keywords: Slide to specific cluster to see the keywords.';
                    for (i = 0; i < x.length; i++) {
						if(
                            reviews[i].includes(key) || 
                            devResponse[i].includes(key)
                            ) {
							x[i] = x_backup[i];
							y[i] = y_backup[i];
						} else {
							x[i] = undefined;
							y[i] = undefined;
						}
                    }
                }
                else {
                    out_text.text = 'Keywords: ' + topics[Number(cluster)];
                    for (i = 0; i < x.length; i++) {
                        if(labels[i] == cluster) {
							if(
                                reviews[i].includes(key) || 
                                devResponse[i].includes(key)
                                ) {
								x[i] = x_backup[i];
								y[i] = y_backup[i];
							} else {
								x[i] = undefined;
								y[i] = undefined;
							}
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }
            source.change.emit();
            """)
    return callback