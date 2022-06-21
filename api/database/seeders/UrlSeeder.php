<?php

namespace Database\Seeders;

use App\Models\Url;
use Illuminate\Database\Seeder;

class UrlSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $handle = fopen("black_list.txt", "r");
        if ($handle) {
            while (($line = fgets($handle)) !== false) {
                Url::updateOrCreate([
                    'url' => $line,
                    'type' => Url::TYPE['BLACK_LIST']
                ]);
            }
            fclose($handle);
        }

        $handle = fopen("white_list.txt", "r");
        if ($handle) {
            while (($line = fgets($handle)) !== false) {
                Url::updateOrCreate([
                    'url' => $line,
                    'type' => Url::TYPE['WHITE_LIST']
                ]);
            }
            fclose($handle);
        }

        // $urls = Url::all();

        // foreach($urls as $url) {
        //     try {
        //         if (preg_match('/^http:\/\//', $url->url)) {
        //             $url->url = preg_replace('/^http:\/\//', 'https://', $url->url);
        //             $url->save();
        //         }
        //     } catch (\Exception $ex) {
        //         continue;
        //     }
        // }
    }
}
