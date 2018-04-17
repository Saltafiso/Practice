module Tire where
data Trie = MakeTrie Char [Trie] 
    deriving Eq

emptyTrie = MakeTrie '.' [MakeTrie '$' []]
showTrie :: Int -> Trie -> String
showTrie level (MakeTrie c []) = "\n" ++ (indent level) ++ [c]
showTrie level (MakeTrie c [subTrie]) = 
    "\n" ++ (indent level) ++ c:(showTrie (level+1) subTrie)
showTrie level (MakeTrie c subTrieList) = 
    "\n" ++ (indent level) ++ 
    c:concat (map (showTrie (level+1)) subTrieList)
indent :: Int -> String
indent n
    | n <= 0 = ""
    | otherwise = "  " ++ (indent (n-1))
instance Show Trie 
    where show t = tail (showTrie 0 t) -- getting rid of extra 
                                       -- newline at beginning
                                       -- of the showTrie result

simpleTrie = 
    MakeTrie '.' [
        MakeTrie 'c' [
            MakeTrie 'a' [
                lastLetter 'n',
                lastLetter 't'
                ]
            ],
        MakeTrie 'd' [
                MakeTrie 'o' [
                    lastLetter 'g'
                ]
            ]
        ]

lastLetter ch = MakeTrie ch [MakeTrie '$' []]

-- part 1
searchWord word (MakeTrie c sub) 
  | word == "" &&  head sub /= MakeTrie '$' [] = False
  | word == "" &&  head sub == MakeTrie '$' [] = True
  | null [(MakeTrie nc nsub)|(MakeTrie nc nsub)<-sub, nc == (head word) && nc /= '$'] = False
  | True = searchWord (tail word) (head [(MakeTrie nc nsub)|(MakeTrie nc nsub)<-sub, nc == (head word)]) && True
-- part 2
wordsInTrie (MakeTrie '$' []) = [""]
wordsInTrie (MakeTrie c [sub]) 
  | c == '.' = wordsInTrie sub
  | True = map (c:) (wordsInTrie sub)
wordsInTrie (MakeTrie c sub) 
  | c == '.' = concat (map wordsInTrie sub)
  | True = map (c:) (concat (map wordsInTrie sub))
-- part 3
addWordToTrie word trie = help2 (word++"$") trie
  where help2(x:xs) (MakeTrie c sub)
          | xs == "" && head sub /= (MakeTrie '$' []) = MakeTrie c (help1((MakeTrie '$' []):sub))
          | xs == "" = MakeTrie c sub
          | null [(MakeTrie nc nsub)|(MakeTrie nc nsub)<-sub, nc == x] = MakeTrie c (help1((help0 (x:xs) []):sub))
          | otherwise = MakeTrie c (help1([(MakeTrie nc nsub)|(MakeTrie nc nsub)<-sub, nc /= x] ++[help2 xs (head [(MakeTrie nc nsub)|(MakeTrie nc nsub)<-sub, nc == x])]))
        help1 [] = []
        help1 ((MakeTrie x sub):xs) = help1 [(MakeTrie c nsub)|(MakeTrie c nsub)<-xs, c<=x] ++ [(MakeTrie x sub)] ++ help1 [(MakeTrie c nsub)|(MakeTrie c nsub)<-xs, c>x] 
        help0 (x:xs) trie 
          | null xs = MakeTrie x []
          | True = MakeTrie x [help0 xs trie] 
-- part4 
createTrie [""] = emptyTrie
createTrie list = foldr addWordToTrie (MakeTrie '.' []) list

webTrie = createTrie ["catnip", "cat", "dog", "cab", "dime", "dim", "candy", "cat", "catalog", "do"]

