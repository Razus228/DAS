import { Injectable, WritableSignal, signal } from '@angular/core';
import { AuthentificationDataI } from '../intefaces/authorization.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthorizationService {

    usersData: WritableSignal<AuthentificationDataI[]> = signal([]);

    constructor() { }

    addUser(data: AuthentificationDataI): void {
        this.usersData.mutate(userList => {
            userList.push(data);
        })
        console.log(this.usersData());
    }
}
