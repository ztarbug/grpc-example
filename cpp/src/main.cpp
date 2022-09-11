#include <iostream>
#include <fstream>

#include "sampleClient.hpp"

using namespace std;
using namespace sampleclient;

int main(int argc, char** argv) {
    cout << "make an API call" << std::endl;;

    MyClient client;
    client.callAPI();
    
    return 0;    
}