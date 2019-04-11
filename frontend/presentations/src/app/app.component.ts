import { Component, Injectable, OnInit } from '@angular/core';


import { Observable } from 'rxjs';
import {TableModule} from 'primeng/table';

@Component({
  selector: 'app-root',
  template: `
  <h2>Presentation List</h2>
  <ul *ngFor="let presentation of presentations">
     <li>{{presentation.title}}</li>
  </ul>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'presentations';
}
export interface Presentation {
  id;
  title;
  thumbnail;
  author;
  createdAt;
}


import { HttpClient} from '@angular/common/http';

@Injectable()
export class PresentationService {
  private _url: string = "127.0.0.1/8000"

  constructor(private http:HttpClient){}

  getPresentations(): Observable<Presentation[]>{
    return this.http.get<Presentation[]>(this._url);
  }
}

export class OrderListDemo implements OnInit{

  presentation: Presentation[];

  public presentations = [];
  
  constructor(private _presentationService: PresentationService) { }

  ngOnInit() {
      this._presentationService.getPresentations().subscribe(
        data => this.presentations = data);
  }
  
}

