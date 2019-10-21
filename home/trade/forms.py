from django import forms

from trade.models import Flags


class FlagsForm(forms.ModelForm):
    class Meta:
        model = Flags
        fields = ["panjivarecordid", "leb", "cites", "high", "iucn", "lacey", "text"]

    @staticmethod
    def insert_from_csv_v2(row):
        panjivarecordid_index = 0
        leb_index = 3
        cites_index = 4
        high_index = 5
        iucn_index = 6
        lacey_index = 7
        text_index = 10

        data = {
            "panjivarecordid": row[panjivarecordid_index],
            "leb": row[leb_index] != "0",
            "cites": row[cites_index] != "0",
            "high": row[high_index] != "0",
            "iucn": row[iucn_index] != "0",
            "lacey": row[lacey_index] != "0",
            "text": row[text_index] != "0",
        }

        Flags.objects.filter(panjivarecordid=data["panjivarecordid"]).delete()

        form = FlagsForm(data)
        if form.is_valid():
            form.save()
        else:
            print(
                "Invalid data saving flags for {} to database".format(
                    row[panjivarecordid_index]
                )
            )
