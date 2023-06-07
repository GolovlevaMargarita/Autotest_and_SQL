import sender_stand_request
def test_track_order_status_code_200():
    track = sender_stand_request.post_order();
    response = sender_stand_request.get_order_by_track(track);
    assert response.status_code == 200