#Reference: https://github.com/MaksimEkin/COVID19-Literature-Clustering/blob/master/lib/call_backs.py
from bokeh.models import CustomJS

# handle the currently selected article
def selected_code():
    code = """
            var reviews = [];
            var ratings = [];
            var reviewPostDate = [];
            var thumbsUps = [];
            cb_data.source.selected.indices.forEach(index => reviews.push(source.data['reviews'][index]));
            cb_data.source.selected.indices.forEach(index => rating.push(source.data['ratings'][index]));
            cb_data.source.selected.indices.forEach(index => reviewPostDate.push(source.data['reviewPostDate'][index]));
            cb_data.source.selected.indices.forEach(index => thumbsUps.push(source.data['thumbsUps'][index]));
            review = "<h4>" + reviews[0].toString().replace(/<br>/g, ' ') + "</h4>";
            rating = "<p1><b>Is review edited?:</b> " + ratings[0].toString().replace(/<br>/g, ' ') + "<br>"
            reviewPostDate = "<b>Review post date</b>" + reviewPostDate[0].toString() + "<br>"
            thumbsUp = "<b>Link:</b> <a href='" + "http://doi.org/" + thumbsUps[0].toString() + "'>" + "http://doi.org/" + thumbsUps[0].toString() + "</a></p1>"
            current_selection.text = review + rating + thumbsUp + reviewPostDate
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
                thumbsUp = data['thumbsUp'];
                reviews = data['review'];
                ratings = data['rating'];
                reviewPostDate = data['reviewPostDate'];
                if (cluster == '10') {
                    out_text.text = 'Keywords: Slide to specific cluster to see the keywords.';
                    for (i = 0; i < x.length; i++) {
						if(thumbsUp[i].includes(key) || 
						titles[i].includes(key) || 
						ratings[i].includes(key) || 
						reviewPostDate[i].includes(key)) {
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
							if(thumbsUp[i].includes(key) || 
							titles[i].includes(key) || 
							ratings[i].includes(key) || 
							reviewPostDate[i].includes(key)) {
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