import pandas


class Ranking:
    def __init__(self, CPM, WPM, words):
        self.new_score = {"CPM": CPM, "WPM": WPM}
        self.new_score_df = pandas.DataFrame(self.new_score, index=[0])
        try:
            self.ranking = pandas.read_csv("ranking.csv")
        except FileNotFoundError:
            self.new_score_df.to_csv("ranking.csv", index=False)
            self.ranking = pandas.read_csv("ranking.csv")
        finally:
            self.new_record = pandas.concat([self.ranking, self.new_score_df])
            self.new_record.to_csv("ranking.csv", index=False)

        CPM_hs = self.new_record.CPM.max()
        WPM_hs = self.new_record.WPM.max()

        words['state'] = 'normal'
        words.delete('1.0', 'end')
        words.insert('2.2', f"End of Time. \nYour score: {WPM}WPM, {CPM}CPM \nHighest record: {WPM_hs}WMP, {CPM_hs}CMP")
        words['state'] = 'disabled'
        words.update()
