int arrayConversion(vector<int> inputArray) {
    using namespace std;
    int count = 0;
    while (inputArray.size() > 1) {
        count++;
        vector<int> tmp;
        if (count % 2 == 1) {
            for (int i = 0; i < inputArray.size() / 2; i++) {
                tmp.push_back(inputArray[2 * i] + inputArray[2 * i + 1]);
            }
            inputArray = tmp;
        } else {
            for (int i = 0; i < inputArray.size() / 2; i++) {
                tmp.push_back(inputArray[2 * i] * inputArray[2 * i + 1]);
            }
            inputArray = tmp;
        }
    }
    return inputArray[0];
}
