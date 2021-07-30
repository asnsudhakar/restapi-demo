from HTTPBinService import HTTPBinService

if __name__ == '__main__':
    http_bin_handler = HTTPBinService()
    encoded_text = 'SFRUUEJJTiBpcyBhd2Vzb21l'

    #Valdiate the base64-url encoded string
    decoded_text = http_bin_handler.test_get_http_req_base64(encoded_text)
    print(decoded_text)
    assert(decoded_text == 'HTTPBIN is awesome')

    name = 'Irdeto'
    value = 10
    #Validate the http cookies date returns properly
    list_cookies = http_bin_handler.test_get_http_cookies(name, value)
    print(list_cookies)
    assert (list_cookies['cookies']['Irdeto'])


    # Validate POST request for delay and verify the elapsed time after response
    response_time = http_bin_handler.test_post_http_deleyed_respose(3)
    assert (response_time > 3)
    print(response_time)

    # validate the PUT request for the deley response and verify the elapsed time
    response_time = http_bin_handler.test_put_http_deleyed_respose(2)
    assert (response_time > 2)
    print(response_time)

    # Validate POST request for http anything and validate the response
    json_response = http_bin_handler.test_post_http_anything()
    print(json_response['json']['job'])
    assert (json_response['json']['job'] == "Automation")

    # Validate the delete anyting and verify the the resource is removed
    delete_response = http_bin_handler.test_delete_http_anything()
    print(delete_response)
    assert (delete_response == 200)


