int[] treeBottom(String tree) {
    if (tree.length() <= 2) return new int [0];
        Queue<String> queue = new LinkedList<>();
        queue.offer (tree);
        List<Integer> list = new ArrayList<>();
        while (!queue.isEmpty()) {
            int size = queue.size();
            list.clear();

            while (size -- > 0) {
                String n = queue.poll();
                n = n.substring(1, n.length() - 1);
                int num = 0, idx = 0;

                while (idx < n.length() && Character.isDigit(n.charAt(idx))) num = 10 * num + (n.charAt(idx ++) - '0');
                list.add (num);

                while (idx < n.length() && n.charAt(idx) == ' ') idx ++;

                // left
                int start = idx;
                idx ++;
                for(int count = 1; idx < n.length() && count != 0; idx ++) {
                    if (n.charAt(idx) == '(') count ++;
                    else if (n.charAt(idx) == ')') count --;
                }

                if (idx - start > 2) queue.offer (n.substring (start, idx));
                while (idx < n.length() && n.charAt(idx) == ' ') idx ++;

                // right
                start = idx;
                idx ++;
                for(int count = 1; idx < n.length() && count != 0; idx ++) {
                    if (n.charAt(idx) == '(') count ++;
                    else if (n.charAt(idx) == ')') count --;
                }

                if (idx - start > 2) queue.offer (n.substring (start, idx));
            }
        }
        int [] ans = new int [list.size()];
        for (int idx = 0; idx < list.size(); idx ++) ans [idx] = list.get (idx);
        return ans;
}
