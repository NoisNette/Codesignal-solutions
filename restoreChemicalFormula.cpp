void getPrefixes(vector<string> &prefixes, const vector<string> &elements, string formula)
{
    for(auto elem : elements) 
    {
        int i;
        for(i=0; i<elem.size(); i++) 
        {
            if(elem[i] != formula[i] && (elem[i]+'A'-'a') != formula[i]) 
            {
                break;
            }
        }
        
        if(i==elem.size()) 
        {
            prefixes.push_back(elem);
        }
    }
}

vector<pair<int, string>> possibleSolutions;

void backTrack(const vector<string> &elements, string formula, vector<string> so_far) 
{
    vector<string> prefixes;

    if(formula == "") 
    { // found solution
        string solution = "";
        for(auto x : so_far) 
        {
            solution += x;
        }
        possibleSolutions.push_back(make_pair(so_far.size(), solution));
        return;
    }

    getPrefixes(prefixes, elements, formula);
    for(auto prefix : prefixes) 
    {
        so_far.push_back(prefix);
        backTrack(elements, formula.substr(prefix.size()), so_far);
        so_far.pop_back();
    }
}

std::string restoreChemicalFormula(std::vector<std::string> elements, std::string formula) 
{
    vector<string> so_far;
    backTrack(elements, formula, so_far);

    std::sort(
        possibleSolutions.begin(), 
        possibleSolutions.end(),
        [](const pair<int, string> &ps1, const pair<int, string> ps2) 
        {
            if(ps1.first != ps2.first) 
                return ps1.first < ps2.first;
            return ps1.second < ps2.second;
        }
    );

    return possibleSolutions[0].second;
}
